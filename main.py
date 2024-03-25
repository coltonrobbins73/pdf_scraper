from scrape_code_blocks import extract_code_blocks
import csv

if __name__ == "__main__":
    pdf_path = r"/mnt/c/Users/colto/Desktop/Textbooks/ISLP_website.pdf"
    code_blocks = extract_code_blocks(pdf_path)
    with open('code_blocks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(code_blocks)
        
