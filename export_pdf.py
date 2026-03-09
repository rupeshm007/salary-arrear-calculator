from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_pdf(results, leave_results, total):
    """
    Create PDF file with arrear calculations
    
    Args:
        results: List of salary arrear results
        leave_results: List of leave surrender results
        total: Total arrear amount
    
    Returns:
        str: Path to created PDF file
    """
    file = "arrear_statement.pdf"
    
    # Create the PDF document
    doc = SimpleDocTemplate(file, pagesize=landscape(A4))
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        alignment=1,  # Center alignment
        spaceAfter=20
    )
    elements.append(Paragraph("Salary Arrear Statement", title_style))
    elements.append(Spacer(1, 0.2 * inch))

    # Salary Arrear Table
    if results:
        elements.append(Paragraph("Salary Arrear Details", styles['Heading2']))
        elements.append(Spacer(1, 0.1 * inch))
        
        # Prepare data for table
        table_data = [["Month", "Old Basic (₹)", "Arrear %", "Arrear (₹)", "Revised Basic (₹)"]]
        for r in results:
            table_data.append([
                r["month"],
                f"{r['basic']:,.0f}",
                f"{r['percent']}%",
                f"{r['arrear']:,.0f}",
                f"{r['revised_basic']:,.0f}"
            ])
        
        # Create table
        table = Table(table_data, colWidths=[1.2*inch, 1.2*inch, 0.8*inch, 1.2*inch, 1.2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        elements.append(Spacer(1, 0.3 * inch))

    # Leave Surrender Table
    if leave_results:
        elements.append(Paragraph("Leave Surrender Arrear", styles['Heading2']))
        elements.append(Spacer(1, 0.1 * inch))
        
        # Prepare data for table
        table_data = [["Year", "Leave Amount (₹)", "35% Arrear (₹)"]]
        for r in leave_results:
            table_data.append([
                r["year"],
                f"{r['amount']:,.0f}",
                f"{r['arrear']:,.0f}"
            ])
        
        # Create table
        table = Table(table_data, colWidths=[1.5*inch, 2*inch, 2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        elements.append(Spacer(1, 0.3 * inch))

    # Total
    if results or leave_results:
        total_style = ParagraphStyle(
            'TotalStyle',
            parent=styles['Heading3'],
            fontSize=14,
            alignment=1,
            textColor=colors.green,
            spaceAfter=20
        )
        elements.append(Paragraph(f"Total Arrear : ₹ {total:,.0f}", total_style))

    # Build PDF
    doc.build(elements)
    
    return file