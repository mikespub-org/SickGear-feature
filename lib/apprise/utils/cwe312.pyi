from .parse import is_hostname as is_hostname, parse_url as parse_url

def cwe312_word(word, force: bool = False, advanced: bool = True, threshold: int = 5):
    """This function was written to help mask secure/private information that
    may or may not be found within Apprise. The idea is to provide a
    presentable word response that the user who prepared it would understand,
    yet not reveal any private information for any potential intruder.

    For more detail see CWE-312 @
       https://cwe.mitre.org/data/definitions/312.html

    The `force` is an optional argument used to keep the string formatting
    consistent and in one place. If set, the content passed in is presumed
    to be containing secret information and will be updated accordingly.

    If advanced is set to `True` then content is additionally checked for
    upper/lower/ascii/numerical variances. If an obscurity threshold is
    reached, then content is considered secret
    """
def cwe312_url(url):
    """This function was written to help mask secure/private information that
    may or may not be found on an Apprise URL. The idea is to not disrupt the
    structure of the previous URL too much, yet still protect the users private
    information from being logged directly to screen.

    For more detail see CWE-312 @
    https://cwe.mitre.org/data/definitions/312.html

    For example, consider the URL: http://user:password@localhost/

    When passed into this function, the return value would be:
    http://user:****@localhost/

    Since apprise allows you to put private information everywhere in it's
    custom URLs, it uses this function to manipulate the content before
    returning to any kind of logger.

    The idea is that the URL can still be interpreted by the person who
    constructed them, but not to an intruder.
    """
