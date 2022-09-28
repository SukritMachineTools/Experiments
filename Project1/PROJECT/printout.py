import os
from fpdf import FPDF
company="RAMADA HOTEL"
address="Jalandhar"
contact="+91 9898989898"

class my_cust_PDF(FPDF):
    def header(self):
        self.set_text_color(76, 2, 159)
        self.set_font('Helvetica', 'B', 20)
        w = self.get_string_width(company) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, company)
        self.ln(10) # line break

        self.set_font('Helvetica', 'B', 12)
        w = self.get_string_width(address) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, address)
        self.ln(10)

        w = self.get_string_width(contact) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, contact)
        self.ln(10)

        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_content(self,data,headings):


        self.set_fill_color(200, 220, 255)
        self.ln()
        self.ln()


        self.set_font('Arial', 'B', 11)
        spacing=1
        col_width = self.w /7.5   # 9 = no of columns +1 to adjust columns to screen
        row_height = self.font_size+4


        # self.set_text_color(150, 56, 255)
        #Table heading
        for i in headings:  # for headings
            self.cell(col_width, row_height * spacing, txt=i, border=1)
        self.ln(row_height * spacing)

        #table body
        self.set_font('Arial', '', 11)
        for row in data:
            for item in row:
                self.cell(col_width, row_height * spacing, txt=str(item), border=1)
            self.ln(row_height * spacing)
        # Line break

        self.ln()


        # Mention in italics
        self.ln()
        self.ln()
        self.ln()
        self.set_font('', 'I')
        text1 = '(---------------------  end of page  -----------------------)'
        w = self.get_string_width(text1) + 6
        self.set_x((210 - w) / 2)
        self.cell(0, 6, text1)

    def print_chapter(self,data,headings):
        self.add_page()
        self.chapter_content(data,headings)

if __name__ == '__main__':
      my_cust_PDF()