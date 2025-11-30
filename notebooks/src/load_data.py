import sparknlp

class LoadData:
    spark = sparknlp.start()
    example = "teste"

    def __init__(self, path: str):
        
        print("Hello")