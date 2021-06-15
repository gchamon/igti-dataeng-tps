from urllib import robotparser
import string
import nltk

nltk.download('punkt')
nltk.download('stopwords')


def solve_instagram_robots():
    instagram_robots = """
    User-agent: Applebot
    Disallow: /api/
    Disallow: /graphql/query/
    Disallow: /publicapi/
    Disallow: /query/
    
    User-agent: baiduspider
    Disallow: /api/
    Disallow: /graphql/query/
    Disallow: /publicapi/
    Disallow: /query/
    
    User-agent: Bingbot
    Disallow: /api/
    Disallow: /graphql/query/
    Disallow: /publicapi/
    Disallow: /query/
    
    User-agent: DuckDuckBot
    Disallow: /api/
    Disallow: /graphql/query/
    Disallow: /publicapi/
    Disallow: /query/
    
    User-agent: Googlebot
    Disallow: /api/
    Disallow: /graphql/query/
    Disallow: /publicapi/
    Disallow: /query/
    """

    robots_parser = robotparser.RobotFileParser()
    robots_parser.parse(instagram_robots.strip().split("\n"))

    print("can Googlebot access `/api/`? " + str(robots_parser.can_fetch("Googlebot", "/api/")))
    print("can Applebot access `/query/`? " + str(robots_parser.can_fetch("Applebot", "/query/")))

def _tokenize(text):
    return (word for word in nltk.word_tokenize(' '.join(text.split("-")))
            if word not in string.punctuation)


def solve_tokenize():
    text_to_tokenize = "Considere o seguinte texto: esse texto refere-se ao enunciado da questão 5"
    tokenized_text = list(_tokenize(text_to_tokenize))
    print(tokenized_text)
    print(len(tokenized_text))


def solve_stem():
    text_to_tokenize = "menino e menina se conheceram quase sem querer. Após se conhecerem"
    tokenized_text = _tokenize(text_to_tokenize)
    stemmed_text = set(_stem(tokenized_text).values())
    print(stemmed_text)
    print(len(stemmed_text))


def solve_stop():
    stopwords = nltk.corpus.stopwords.words('portuguese')
    text_to_tokenize = "recuperação recuperam alunos que precisam ser recuperados"
    tokenized_text = _tokenize(text_to_tokenize)
    text_without_stopwords = {word for word in tokenized_text if word not in stopwords}
    stemmed_text = _stem(text_without_stopwords)
    print(stemmed_text)
    print(len(stemmed_text))


def _stem(text_to_stem):
    snowball_stemmer = nltk.SnowballStemmer("portuguese")
    stemmed_text = {word: snowball_stemmer.stem(word) for word in text_to_stem}
    return stemmed_text


if __name__ == "__main__":
    solve_instagram_robots()
    solve_tokenize()
    solve_stem()
    solve_stop()
