class output(object):
    """ Class that handles database output formatting.
    Takes tuples from sql output and transforms them
    as needed.
    """

    def text(sql):
        output = []
        for row in sql:
            line = []
            for column in row:
                line.append(str(column))

            output.append(': '.join(line))

        return '\n'.join(output)
