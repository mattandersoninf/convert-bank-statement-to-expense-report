import PyPDF2
import argparse
import json
import sys
import pdftotext


def parse_arguments():
    parser = argparse.ArgumentParser(description='This script tries to read in a PDF statement.')
    parser.add_argument('path', help='Absolute\\Path\\To\\Statement.pdf')
    parser.add_argument('--verbose', '-vb', help='Turn on verbose logging')
    args = parser.parse_args()

    return args


def get_google_account_keys_file_from_json(keys_json_file='config.json'):
    # get google account keys
    try:
        with open(keys_json_file) as f:
            myjson = json.load(f)
            return myjson
    except FileNotFoundError as fe:
        print("---NO CONFIG FILE FOUND -- STOPPING EXECUTION---")
        print(fe)
        sys.exit(0)


class BankStatementParser:

    """This class works on reading / parsing the information from the input PDF"""

    def __init__(self, pdfpath):
        self.pdfpath = pdfpath
        self.pages = {}

    def get_pdf_file(self):
        try:
            with open(self.pdfpath, 'rb') as f:
                pdf = pdftotext.PDF(f)
        except FileNotFoundError as fe:
            print('File not found with path: ' + self.pdfpath)
            sys.exit(0)
        except Exception as e:
            print('Unexpected error occured!')
            print(e)
            sys.exit(0)
        for pagenum in range(len(pdf)):
            self.pages[pagenum + 1] = pdf[pagenum]

    def print_pdf_page(self, pagenum):
        print(self.pages[pagenum])

    def get_page_numbers(self):
        for pagenum in sorted(self.pages.keys()):
            print('Page {}/{}'.format(pagenum, len(self.pages.keys())))


def main():
    json_file = get_google_account_keys_file_from_json()
    statement_path = json_file['runtime']['bank_statement_pdf']
    statement_parser = BankStatementParser(statement_path)
    statement_parser.get_pdf_file()
    statement_parser.print_pdf_page(1)
    statement_parser.get_page_numbers()


if __name__ == '__main__':
    main()
