from abc import ABC , abstractmethod

class File(ABC):

    @abstractmethod
    def file_handling(self):
     pass 


class Pdf(File):
    def file_handling(self):
        print("Pdf file is called")

class Excel(File):
    def file_handling(self):
        print("Excel file is called")


pdf=Pdf()
pdf.file_handling()

excel=Excel()
excel.file_handling()


    