<<<<<<< HEAD
<<<<<<< HEAD
# This file must be used with "source <venv>/bin/activate.fish" *from fish*
# (https://fishshell.com/); you cannot run it directly.

function deactivate  -d "Exit virtual environment and return to normal shell environment"
=======
=======
>>>>>>> 30631c49693a5289a9d1a1b6e48c0200e953b539
# This file must be used with ". bin/activate.fish" *from fish* (http://fishshell.org)
# you cannot run it directly

function deactivate  -d "Exit virtualenv and return to normal shell environment"
<<<<<<< HEAD
>>>>>>> d87ae31b99d345d0a1f00aaa964f6b8a373531c3
=======
>>>>>>> 30631c49693a5289a9d1a1b6e48c0200e953b539
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH $_OLD_VIRTUAL_PATH
        set -e _OLD_VIRTUAL_PATH
    end
    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
        functions -e fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
    end

    set -e VIRTUAL_ENV
    if test "$argv[1]" != "nondestructive"
<<<<<<< HEAD
<<<<<<< HEAD
        # Self-destruct!
=======
        # Self destruct!
>>>>>>> d87ae31b99d345d0a1f00aaa964f6b8a373531c3
=======
        # Self destruct!
>>>>>>> 30631c49693a5289a9d1a1b6e48c0200e953b539
        functions -e deactivate
    end
end

<<<<<<< HEAD
<<<<<<< HEAD
# Unset irrelevant variables.
=======
# unset irrelevant variables
>>>>>>> d87ae31b99d345d0a1f00aaa964f6b8a373531c3
=======
# unset irrelevant variables
>>>>>>> 30631c49693a5289a9d1a1b6e48c0200e953b539
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/jordany/Documentos/estanteVirtual/venv"

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

<<<<<<< HEAD
<<<<<<< HEAD
# Unset PYTHONHOME if set.
=======
# unset PYTHONHOME if set
>>>>>>> d87ae31b99d345d0a1f00aaa964f6b8a373531c3
=======
# unset PYTHONHOME if set
>>>>>>> 30631c49693a5289a9d1a1b6e48c0200e953b539
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # fish uses a function instead of an env var to generate the prompt.

<<<<<<< HEAD
<<<<<<< HEAD
    # Save the current fish_prompt function as the function _old_fish_prompt.
    functions -c fish_prompt _old_fish_prompt

    # With the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Save the return status of the last command.
        set -l old_status $status

        # Output the venv prompt; color taken from the blue of the Python logo.
        printf "%s%s%s" (set_color 4B8BBE) "(venv) " (set_color normal)

        # Restore the return status of the previous command.
        echo "exit $old_status" | .
        # Output the original/"old" prompt.
=======
=======
>>>>>>> 30631c49693a5289a9d1a1b6e48c0200e953b539
    # save the current fish_prompt function as the function _old_fish_prompt
    functions -c fish_prompt _old_fish_prompt

    # with the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Save the return status of the last command
        set -l old_status $status

        # Prompt override?
        if test -n "(venv) "
            printf "%s%s" "(venv) " (set_color normal)
        else
            # ...Otherwise, prepend env
            set -l _checkbase (basename "$VIRTUAL_ENV")
            if test $_checkbase = "__"
                # special case for Aspen magic directories
                # see https://aspen.io/
                printf "%s[%s]%s " (set_color -b blue white) (basename (dirname "$VIRTUAL_ENV")) (set_color normal)
            else
                printf "%s(%s)%s" (set_color -b blue white) (basename "$VIRTUAL_ENV") (set_color normal)
            end
        end

        # Restore the return status of the previous command.
        echo "exit $old_status" | .
<<<<<<< HEAD
>>>>>>> d87ae31b99d345d0a1f00aaa964f6b8a373531c3
=======
>>>>>>> 30631c49693a5289a9d1a1b6e48c0200e953b539
        _old_fish_prompt
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end
