class CurrencyConverterTool:
    def __init__(self):
        pass

    def setup_tools(self):
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
            """Convert currency from one to another"""
            # Here you would implement the actual conversion logic, possibly using an API
            # For demonstration purposes, let's assume a fixed conversion rate
            conversion_rate = 1.2  # This is just a placeholder
            converted_amount = amount * conversion_rate
            return f"{amount} {from_currency} is approximately {converted_amount} {to_currency}"

        self.currency_converter_tool_list = [convert_currency]