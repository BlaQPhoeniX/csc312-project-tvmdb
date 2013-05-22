$(document).ready(function() {
    $('#calendar').fullCalendar({
        // Options here
        events : '/ajax/events/',
        header : {
          left : 'prev,next today',
          center : 'title',
          right : 'month,agendaWeek,agendaDay'
        },
        eventColor : '#777',
        timeFormat : {
          agenda : 'H:mm{ - H:mm}',
          '' : 'H:mm'
          },
    })
});

$(document).ready(function(){
    $('#sub').click(function(){
        var btn = $(this);
        $.get('/ajax/subscribe/'+this.value).done(function(){
            btn.toggle(400);
            $('#unsub').toggle(400);})
    })
});

$(document).ready(function(){
    $('#unsub').click(function(){
        var btn = $(this);
        $.get('/ajax/unsubscribe/'+this.value).done(function(){
            btn.toggle(400);
            $('#sub').toggle(400);})
    })
});

$(document).ready(function(){
    $(':checkbox').change(function(){
        if (this.checked){
            $.get('/ajax/subscribe/'+this.value);}
        else{
            $.get('/ajax/unsubscribe/'+this.value);}
    })
});

$(document).ready(function(){
    $('.search-query').typeahead({
        source : function (query, process) {
          $.get('/ajax/search', {q : query}, function(data){
            series = [];
            map = {};

            $.each(data.results, function (i, media) {
                map[media.title] = media;
                series.push(media.title);
            });
            process(series);})
        },
        updater : function (item) {
             mid = map[item].id;
             window.location = '/media/'+mid;
             return item;}
    });
});
