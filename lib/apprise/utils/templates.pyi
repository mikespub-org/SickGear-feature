class TemplateType:
    """Defines the different template types we can perform parsing on."""
    RAW: str
    JSON: str

def apply_template(template, app_mode=..., **kwargs):
    """Takes a template in a str format and applies all of the keywords and
    their values to it.

    The app$mode is used to dictact any pre-processing that needs to take place
    to the escaped string prior to it being placed.  The idea here is for
    elements to be placed in a JSON response for example should be escaped
    early in their string format.

    The template must contain keywords wrapped in in double squirly braces like
    {{keyword}}.  These are matched to the respected kwargs passed into this
    function.

    If there is no match found, content is not swapped.
    """
