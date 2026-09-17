from fpdf import FPDF

def main():
    name = input("Name: ").strip()

    # Create an A4 PDF in portrait orientation using millimetres
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # Document title
    pdf.set_font("Helvetica", style="B", size=28)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(
        w=0,
        h=20,
        text="CS50 Shirtificate",
        align="C"
    )

    # Shirt image
    image_width = 190
    image_x = (pdf.w - image_width) / 2

    pdf.image(
        "shirtificate.png",
        x=image_x,
        y=50,
        w=image_width
    )

    # Name displayed over the shirt
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)

    pdf.set_xy(0, 100)
    pdf.cell(
        w=pdf.w,
        h=10,
        text=f"{name}",
        align="C"
    )

    # Create the final file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()