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
        if [[ -f "$f" ]]; then
            echo "running ${f}"
            python3 ${f}
        fi
    done

    # run the julia files if we've got any
    for f in ${d}*.jl ; do
        if [[ -f "$f" ]]; then
            echo "running ${f}"
            julia ${f}
        fi
    done

    # run the go files if we've got any
    for f in ${d}*.go ; do
        if [[ -f "$f" ]]; then
            echo "running ${f}"
            go run ${f}
        fi
    done
done
