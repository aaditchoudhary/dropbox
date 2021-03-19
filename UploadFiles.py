import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AtTQrsxBNvE-BmLsb4EIHtPYDFY2qQKC9J8Zz2LBK5KsYTOBL6H4hN83qAcThgl06diS4sRLoxqMFRszJJlg6jh5x5gHJ6jbBMgO1Jft73kSLukiMl-mIBSsbxFRnMH_-UB1_dA'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/a2z/Desktop/python/2.txt'
    file_to = 'C:/Users/a2z/Dropbox'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()