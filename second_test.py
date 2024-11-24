from __init__ import process_adjectives 
def test_word_filter():
    result = process_adjectives("крута великий миле веселі гарна", "comparative")
    assert result == " ".join(["крутіша", "більший", "миліше", "веселіші", "краща"])
 
def test_word_filter():
    result = process_adjectives("крута великий миле веселі гарна", "superlative")
    assert result == " ".join(["найкрутіша", "найбільший","наймиліше", "найвеселіші", "найкраща"])
