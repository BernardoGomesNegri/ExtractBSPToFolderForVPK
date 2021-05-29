class Args:
    """Represents arguments that can be passed to the application
    ### Fields
    * input - str
    * output - str
    * parallel - bool"""
    def __init__(self, input: str, output: str, parallel: bool) -> None:
        self.input = input
        self.output = output
        self.parallel = parallel