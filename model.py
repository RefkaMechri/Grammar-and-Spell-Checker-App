from textblob import TextBlob
import language_tool_python

class SpellCheckerModule:
    def __init__(self):
        # Initialize the grammar checker using language_tool_python
        self.grammar_check = language_tool_python.LanguageTool('en-US') 

    def correct_spell(self, text):
        """
        Corrects the spelling of each word in the input text.
        
        Parameters:
            text (str): The input text with possible spelling errors.
            
        Returns:
            str: The text with corrected spelling.
        """
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        """
        Checks and corrects the grammar of the input text.
        
        Parameters:
            text (str): The input text with possible grammatical errors.
            
        Returns:
            tuple: A tuple containing a list of found mistakes and their count.
        """
        matches = self.grammar_check.check(text)
        foundmistakes = [match.context for match in matches]
        foundmistakes_count = len(foundmistakes)
        return foundmistakes, foundmistakes_count

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Helo world. I like mashine learning. appple. bananana"
    print("Corrected Spelling:", obj.correct_spell(message))
    mistakes, mistakes_count = obj.correct_grammar(message)
    print("Found Mistakes:", mistakes)
    print("Number of Mistakes:", mistakes_count)
