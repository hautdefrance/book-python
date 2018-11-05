def make_paragraph(fn):

    def decorator(*args, **kwargs):
        value = fn(*args, **kwargs)
        print(f'<p>{value}</p>')
        return value

    return decorator


class HTMLReport:

    @make_paragraph
    def first_method(self, *args, **kwargs):
        return 'First Method'

    @make_paragraph
    def second_method(self, *args, **kwargs):
        return 'Second Method'


if __name__ == "__main__":
    x = HTMLReport()
    x.first_method()
    x.second_method()

"""
<p>First Method</p>
<p>Second Method</p>
"""