import os
from PyPDF2 import PdfMerger

def merge_numbered_pdfs(input_folder="input", output_folder="output", output_name="merged_output.pdf"):
    # Make sure folders exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    merger = PdfMerger()

    # Get all PDFs in the input folder
    pdfs = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

    # Only get PDFs named like 1.pdf, 2.pdf, 3.pdf
    numbered_pdfs = []
    for f in pdfs:
        try:
            num = int(os.path.splitext(f)[0])  # extract number (filename without extension)
            numbered_pdfs.append((num, f))
        except ValueError:
            pass  # ignore PDFs that are not purely numbered

    # Sort files numerically
    numbered_pdfs.sort(key=lambda x: x[0])

    if not numbered_pdfs:
        print("No numbered PDFs found in the input folder.")
        return

    # Merge them
    for num, pdf in numbered_pdfs:
        path = os.path.join(input_folder, pdf)
        print(f"Adding: {pdf}")
        merger.append(path)

    # Save output
    output_path = os.path.join(output_folder, output_name)
    merger.write(output_path)
    merger.close()
    print(f"\nMerged PDF saved as: {output_path}")

if __name__ == "__main__":
    merge_numbered_pdfs()
