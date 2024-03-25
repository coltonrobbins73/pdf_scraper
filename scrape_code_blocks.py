import fitz  # Importing PyMuPDF library for handling PDF files

def is_code_line(text):
    """
    Determines if a line is part of a code block.
    
    A line is considered a part of a code block if it starts with "In [".
    
    :param text: The text of the line to check.
    :return: True if the line is part of a code block, False otherwise.
    """
    return text.startswith("In [")

def extract_code_blocks(pdf_path):
    """
    Extracts code blocks from a PDF file within a specified range of pages.
    
    This function processes the PDF file to identify and extract code blocks, which are
    determined by specific font names and text patterns. It handles the transition between
    code blocks and comments, formatting them appropriately.
    
    :param pdf_path: The file path to the PDF document to be processed.
    :return: A list containing strings of extracted code blocks and comments.
    """
    code_blocks = []  # Stores all extracted code blocks
    current_block = []  # Accumulates lines for the current code block
    collecting_code = False  # Flag to indicate if currently collecting code lines
    comment_collect = False  # Flag to indicate if currently collecting comment lines

    with fitz.open(pdf_path) as doc:
        for page_num in range(50,len(doc)):  # Specify your page range
            page = doc.load_page(page_num)
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if 'lines' in block:  # Ensure the block contains lines
                    for line in block["lines"]:
                        if line["spans"]:  # Check if there are spans in the line
                            first_span = line["spans"][0]
                            font_name = first_span["font"]
                            line_text = "".join(span["text"] for span in line["spans"])
                            if len(line_text) < 3:
                                continue
                            if is_code_line(line_text):
                                # Start collecting code lines
                                collecting_code = True
                                line_text = line_text.split("]: ", 1)[1] if "]: " in line_text else line_text
                            elif font_name in ["LMRoman12-Italic"]:
                                collecting_code = False
                                comment_collect = False
                                current_block.append('--------------------')
                            elif font_name in ["LMRoman10-Regular", "LMRoman9-Regular", "LMRoman10-Bold", "LMRoman9-Bold"]:
                                comment_collect = True
                                collecting_code = False

                            # Collect code or comment lines based on the current state
                            if collecting_code:
                                current_block.append(line_text)
                            elif comment_collect:
                                current_block.append('# ' + line_text)

            # Add the last code block if it's not empty
            if current_block:
                code_blocks.append("\n".join(current_block))
                current_block = []  # Reset for the next page/block

    return code_blocks
