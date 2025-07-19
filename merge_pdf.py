from PyPDF2 import PdfMerger

def merge_pdf(file1, file2, file3, merged_file):
    merger = PdfMerger()

    with open(file1, "rb") as f1:
        merger.append(f1)

    with open(file2, "rb") as f2:
        merger.append(f2)

    with open(file3, "rb") as f3:
        merger.append(f3)

    with open(merged_file, "wb") as result:
        merger.write(result)

    print(f"All content of {file1}, {file2}, {file3} are merged into {merged_file}")

merge_pdf("jassi.adhar(1).pdf", "jassi.adhar(2).pdf", "jassi.adhar(3).pdf", "merged_file.pdf")
