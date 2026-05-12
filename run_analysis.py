#!/usr/bin/env python3
"""
Script to run the Jupyter notebook and export results.
This script executes the Python analysis notebook and exports it to HTML and/or PDF formats.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_notebook_and_export(notebook_path, output_format='html'):
    """
    Execute a Jupyter notebook and export it to specified format(s).
    
    Args:
        notebook_path (str): Path to the notebook file
        output_format (str or list): Format(s) to export to ('html', 'pdf', 'md')
    
    Returns:
        bool: True if successful, False otherwise
    """
    notebook_path = Path(notebook_path)
    
    if not notebook_path.exists():
        print(f"Error: Notebook not found at {notebook_path}")
        return False
    
    # Ensure output formats are in a list
    if isinstance(output_format, str):
        output_format = [output_format]
    
    # Create output directory if it doesn't exist
    output_dir = notebook_path.parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    base_output_path = output_dir / notebook_path.stem
    
    print(f"Running notebook: {notebook_path}")
    print(f"Output directory: {output_dir}")
    
    try:
        # Execute the notebook
        execute_cmd = [
            'jupyter', 'nbconvert',
            '--to', 'notebook',
            '--execute',
            '--ExecutePreprocessor.timeout=600',
            '--output', str(base_output_path / 'executed'),
            str(notebook_path)
        ]
        
        print(f"\nExecuting notebook...")
        subprocess.run(execute_cmd, check=True, capture_output=True)
        print("✓ Notebook executed successfully")
        
        # Export to requested formats
        for fmt in output_format:
            export_cmd = [
                'jupyter', 'nbconvert',
                '--to', fmt,
                '--output', str(base_output_path),
                str(notebook_path)
            ]
            
            print(f"Exporting to {fmt.upper()}...")
            subprocess.run(export_cmd, check=True, capture_output=True)
            print(f"✓ Exported to {fmt.upper()}: {base_output_path}.{fmt}")
        
        print(f"\n✓ All operations completed successfully!")
        print(f"Results saved to: {output_dir}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error executing notebook: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


if __name__ == "__main__":
    # Get notebook path from command line or use default
    notebook_file = sys.argv[1] if len(sys.argv) > 1 else "python_analysis.ipynb"
    
    # Get export format(s) from command line or use defaults
    export_formats = sys.argv[2:] if len(sys.argv) > 2 else ['html', 'md']
    
    # Change to the script's directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Run the notebook
    success = run_notebook_and_export(
        notebook_file,
        output_format=export_formats
    )
    
    sys.exit(0 if success else 1)
