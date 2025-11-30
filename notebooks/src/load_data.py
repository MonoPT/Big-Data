import sparknlp

class LoadData:
    def __init__(self, path: str):
        self.spark = sparknlp.start()
        self.example = "teste"
        print("Hello")