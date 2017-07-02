var year = 2017;
window.onload = function(){
    //[calendarMonth] is capture in the bottom of calenar.html
    //Events value is capture in the bottom of calendar.html
    fillCalendar(events);

};

function fillCalendar(jsonEvent){
    dayName = ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'];
    ids = [];
    days = [];
    dropOffTime = [];
    names = [];
    locations = [];
    items = [];

    jsonEvent.forEach(function(event){
        ids.push(event.pk);
        days.push(event.fields.event_date.replace(new RegExp('-', 'g'), '/'));
        names.push(event.fields.event_name);
        dropOffTime.push(event.fields.drop_off_time);
    });

    var newHTML = "";
    var dayOfWeekIndex = 0;
    for(var d=(1-fillBegin(calendarMonth,year));d<=(daysInMonth(getMonthNumber(calendarMonth),year)+fillEnd(calendarMonth,year));d++){
        var eventDay = getDayNumber(days[0]);
        if(dayOfWeekIndex===0){
            newHTML += "<div class='row'>";
        }
        newHTML +="<div class='day'>";
        newHTML +="<p class='number'><span class='insideDayName'>"+dayName[dayOfWeekIndex]+"</span>";
        if(d>0 && d<= (daysInMonth(getMonthNumber(calendarMonth),year))){
            newHTML += d;
        }else{
            newHTML +="-";
        }
        newHTML+= "</p>";
        newHTML +="<ul class='events'>";
        if(eventDay===d){
            newHTML +="<li><a id='"+ids[0]+"' href='edit/"+ids[0]+"'>"+names[0]+" - "+dropOffTime[0]+"</a></li>";
            days.shift();
            ids.shift();
            names.shift();
            dropOffTime.shift();
        }else{
            newHTML +="<li><a></a></li>";
        }
        newHTML +="</ul>";
        newHTML +="</div>";
        if(dayOfWeekIndex===6){
            newHTML += "</div>";
            dayOfWeekIndex=0;
        }else{
            dayOfWeekIndex++;
        }
    }
    $('.calendar div:last').after(newHTML);
}



function getDayNumber(date){
  return new Date(date).getDate();
}

function getMonthNumber(month){
  return new Date(Date.parse(month+" 1, 2017")).getMonth()+1;
}

function daysInMonth(month, year) {
  return new Date(year, month, 0).getDate();
}

function fillBegin(month,year){
    var date = new Date(month+"/01/"+year);
    var firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
    console.log(firstDay.getDay());
    return firstDay.getDay();
}

function fillEnd(month,year){
    var date = new Date(month+"/01/"+year);
    var lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
    console.log(6-lastDay.getDay());
    return 6-lastDay.getDay();
}