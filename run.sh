for d in */ ; do
    # from https://stackoverflow.com/questions/9018723/what-is-the-simplest-way-to-remove-a-trailing-slash-from-each-parameter
    #
    # you can use the ${parameter%word} expansion that is detailed here
    # https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Parameter-Expansion
    # e.g. echo ${@%/}
    echo "--------------------"
    echo "Day ${d%/}"
    echo "--------------------"
    
    # run the python files if we've got any
    for f in ${d}*.py ; do
        echo "running ${f}"
        python3 ${f}
    done

    # run the julia files if we've got any
    for f in ${d}*.jl ; do
        echo "running ${f}"
        julia ${f}
    done
done
