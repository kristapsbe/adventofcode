for d in */ ; do
    # from https://stackoverflow.com/questions/9018723/what-is-the-simplest-way-to-remove-a-trailing-slash-from-each-parameter
    #
    # you can use the ${parameter%word} expansion that is detailed here
    # https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Parameter-Expansion
    # e.g. echo ${@%/}
    echo "--------------------"
    echo "Day ${d%/}"
    echo "--------------------"
    
    for f in ${d}*.py ; do
        echo "running ${f}"

        # just gonna go with one pre-defined filenames per language
        python3 ${d}main.py
    done
done
