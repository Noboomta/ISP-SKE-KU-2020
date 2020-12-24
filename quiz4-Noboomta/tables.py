"""
This code creates tables in either HTML or Markdown format.
We plan to add reStructuredText and other formats later.
But the code needs refactoring first.

Refactor:

1. Replace Conditional Logic with Polymorphism.
   Use a class hierarchy, not an Enum.

   Add the new classes after the Table class.

2. Replace the Table constructor with a factory method.
   table = Table.create_table("HTML")

   > Revise the code in __main__ to use the factory method.

When you are done, there should not be a tabletype attribute,
but will have a tabletype parameter (or similar) in the factory method.
"""

class Table:
    """Create an HTML or Markdown table with formatting.

    The tabletype should be 'HTML' or 'Markdown'.
    """
    @classmethod
    def create_table(cls, tabletype):
        if tabletype == "HTML":
            return HTMLTable()
        elif tabletype == "Markdown":
            return MarkdownTable()

    def __str__(self):
        """Return the formatted table data."""
        return self.result

    @classmethod
    def join(cls, prefix, infix, postfix, data) -> str:
        """Join elements of data with each element separated by infix.
        Prepend the prefix and append postfix to the result.
        
        This method is for internal use in the class.
        """
        return prefix + infix.join(data) + postfix

class HTMLTable(Table):
    """Class of HTMLTable inherited the Table class."""

    def __init__(self):
        self.result = "<table>\n"

    def add_header(self, *column_headers):
        """Add a header row to the table.

        column_headers - string values for the table column headers
        """
        header = Table.join("<tr><th>", "</th> <th>", "</th></tr>", 
                            column_headers)
            
        self.result += header + '\n'

    def add_row(self, *row_data):
        """Add a row of values to the table. 

        row_data are string values to put in the columns, one per column.
        """
        row = Table.join("<tr><td>", "</td> <td>", "</td></tr>", row_data)
        self.result += row + '\n'

    def end_table(self):
        """Finish and close the table."""
        self.result += "</table>\n"


class MarkdownTable(Table):
    """Class of MarkdownTable inherited the Table class."""

    def __init__(self):
        self.result = ""
        self.column_widths = ""

    def add_header(self, *column_headers):
        """Add a header row to the table.

        column_headers - string values for the table column headers
        """
        self.column_widths = [len(header) for header in column_headers]
        header = Table.join("| ", " | ", " |\n", column_headers)
        # and then a row of dashes
        header += Table.join("|", "|", "|",
                        ['-'*(width+2) for width in self.column_widths])
        self.result += header + '\n'
    
    def add_row(self, *row_data):
        """Add a row of values to the table. 

        row_data are string values to put in the columns, one per column.
        """
        if not self.column_widths:
            self.column_widths = [len(data) for data in row_data]
        values = [f"{data:{w}}" for (data,w) in zip(row_data,self.column_widths)]
        row = Table.join("| ", " | ", " |", values)
        self.result += row + '\n'

    def end_table(self):
        """Finish and close the table."""
        pass


if __name__ == '__main__':
    table = Table.create_table("Markdown")
    table.add_header("First Name", "Last Name", "E-mail Address")
    table.add_row("Bill", "Gates", "bill@msft.com")
    table.add_row("Taksin", "Shinawat", "shin@ais.co.th")
    table.end_table()
    print(table)

