DJANGO_ROOT="G:/eydean/boilerplate"
REACT_ROOT="G:\eydean\boilerplate\frontend"
ENV_ROOT="G:\eydean\env\Scripts\activate"
run_django_server() {
    . "$ENV_ROOT"
    echo "Django root directory: $DJANGO_ROOT"
    cd "$DJANGO_ROOT"
    python manage.py runserver
}

run_react_server(){
    echo "React root directory: $REACT_ROOT"
    cd "$REACT_ROOT"
    npm start

}

run_both_server(){
    run_django_server
    # run_react_server


}

merge_prj(){
    cd "$REACT_ROOT"
    npm run build
    run_django_server
}

# run_both_server
# merge_prj
run_django_server
# run_react_server