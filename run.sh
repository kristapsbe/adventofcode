# run a python script that downloads all of the input files if they're not there

for d in */ ; do
    # from https://stackoverflow.com/questions/9018723/what-is-the-simplest-way-to-remove-a-trailing-slash-from-each-parameter
    #
    # you can use the ${parameter%word} expansion that is detailed here
    # https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Parameter-Expansion
    # e.g. echo ${@%/}
    echo "--------------------"
    echo "Day ${d%/}"
    echo "--------------------"
    
    if command -v python3 > /dev/null; then # make sure we've got python
        # run python files if we've got any
        for f in ${d}*.py ; do
            if [[ -f "$f" ]]; then
                echo "running ${f}"
                python3 ${f}
            fi
        done
    fi

    if command -v julia > /dev/null; then # make sure we've got julia
        # run julia files if we've got any
        for f in ${d}*.jl ; do
            if [[ -f "$f" ]]; then
                echo "running ${f}"
                julia ${f}
            fi
        done
    fi

    if command -v go > /dev/null; then # make sure we've got go
        # run go files if we've got any
        for f in ${d}*.go ; do
            if [[ -f "$f" ]]; then
                echo "running ${f}"
                go run ${f}
            fi
        done
    fi

    if command -v clisp > /dev/null; then # make sure we've got lisp
        # run lisp files if we've got any
        for f in ${d}*.lisp ; do
            if [[ -f "$f" ]]; then
                echo "running ${f}"
                clisp ${f}
            fi
        done
    fi

    if command -v swipl > /dev/null; then # make sure we've got prolog
        # run prolog files if we've got any
        for f in ${d}*.pl ; do
            if [[ -f "$f" ]]; then
                echo "running ${f}"
                swipl -s ${f}
            fi
        done
    fi
done
