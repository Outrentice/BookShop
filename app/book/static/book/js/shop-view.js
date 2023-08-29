//String.prototype.replaceAt = function(index, replacement) {
//    return this.substring(0, index) + replacement + this.substring(index + replacement.length);
//}
//
//
//var grid_button = document.getElementById('grid-view-but')
//
//grid_button.addEventListener('click', (event) => {
//    if ( $("#list-view-but").hasClass('active') ){
//        $("#list-view-but").removeClass('active');
//    }
//    if ( !$("#grid-view-but").hasClass('active') ){
//        $("#grid-view-but").addClass('active');
//    }
//
//    if ( $("#list-view").hasClass('active') ){
//        $("#list-view").removeClass('active');
//    }
//    if ( $("#list-view").hasClass('show') ){
//        $("#list-view").removeClass('show');
//    }
//    if ( !$("#grid-view").hasClass('show') && !$("#grid-view").hasClass('active')  ) {
//        $("#grid-view").addClass('active show');
//    }
//
//    var href = document.location.href
//
//    if (href.indexOf("view=") >= 0) {
//        var index_view = href.indexOf("view=") + 5
//        href = href.replaceAt(index_view, 'grid')
//    }
//    else {
//        href += ((href.indexOf("?") >= 0) ? '&' : '?') + 'view=grid'
//    }
//
//    window.history.pushState( {} , '', href );
//
//})
//
//var list_button = document.getElementById('list-view-but')
//
//list_button.addEventListener('click', (event) => {
//    if ( $("#grid-view-but").hasClass('active') ){
//        $("#grid-view-but").removeClass('active');
//    }
//    if ( !$("#list-view-but").hasClass('active') ){
//        $("#list-view-but").addClass('active');
//    }
//
//    if ( $("#grid-view").hasClass('active') ){
//        $("#grid-view").removeClass('active');
//    }
//    if ( $("#grid-view").hasClass('show') ){
//        $("#grid-view").removeClass('show');
//    }
//    if ( !$("#list-view").hasClass('show') && !$("#list-view").hasClass('active')  ) {
//        $("#list-view").addClass('active show');
//    }
//
//    var href = document.location.href
//
//    if (href.indexOf("view=") >= 0) {
//        var index_view = href.indexOf("view=") + 5
//        href = href.replaceAt(index_view, 'list')
//    }
//    else {
//        href += ((href.indexOf("?") >= 0) ? '&' : '?') + 'view=list'
//    }
//
//    window.history.pushState( {} , '', href );
//})


function change_count(el, book_id) {
    var value = el.value
    if (el.value < 0) { value = 1 }
    window.location.replace('change/' + book_id + '/' + value);
}

function search() {
    input = $('#search')
    console.log(input)
}
