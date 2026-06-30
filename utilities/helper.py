class Helper:

    @staticmethod
    def normalize_text(text):

        return text.strip().lower()

    @staticmethod
    def contains(expected, actual):

        return expected.lower() in actual.lower()