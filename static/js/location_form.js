var counties = new Array();
var city = new Array();
var city_zipCode = [];
window.onload = function(){
    //editableLocation capture in main template
    function loadStates(){
       return $.getJSON(static+'js/states.json');
    }

    loadStates().done( function(json) {
        json.forEach(function(value,index){
            var opt = document.createElement('option');
            opt.value = value.abbreviation;
            opt.innerHTML = value.name.toUpperCase();
            document.getElementById("id_state").appendChild(opt);
        });
        document.getElementById("id_state").value = "FL";
        loadCounties();
    });

    document.getElementById("id_state").onchange = function(){loadCounties();};
    document.getElementById("id_county").onchange = function(){loadCities();};
    document.getElementById("id_city").onchange = function(){loadZipCode()};
    $("#id_county").autocomplete();
}

function loadCounties() {
    city = new Array();
    state = document.getElementById("id_state");
    $.getJSON(static + 'js/cities.json').done(function (json) {
        json.result.forEach(function (data, index) {
            if (state.value == data.State) {
                if( !counties.includes(data.County)){
                    counties.push(data.County);
                }
                city.push(data);
            }
        });
        city.sort();
        counties.sort();
        counties.forEach(function(data){
            var opt = document.createElement('option');
            opt.value = data;
            opt.innerHTML = data;
            document.getElementById("id_county").appendChild(opt);
        });

        if(!editableLocation){
            document.getElementById("id_county").value = "HILLSBOROUGH";
        }else{
            document.getElementById("id_county").value = editableCounty;
        }
        loadCities();
    });
}

function loadCities(){
    $("#id_city").empty();
    county = document.getElementById("id_county");
    newCity = new Array();
    city.forEach(function(c){
        if(c.County == county.value && !newCity.includes(c.City)){
            newCity.push(c.City);
            objCZ = new Object();
            objCZ['city']=c.City;
            objCZ['zipcode']=c.Zipcode;
            city_zipCode.push(objCZ);
        }
    });
    newCity.sort();
    newCity.forEach(function(city){
       var opt = document.createElement('option');
       opt.value = city;
       opt.innerHTML = city;
       document.getElementById('id_city').appendChild(opt);
    });
    if(!editableLocation){
        document.getElementById("id_city").value = "TAMPA";
    }else{
        document.getElementById("id_city").value = editableCity;
    }
    loadZipCode();
}

function loadZipCode(){
    cityName = document.getElementById("id_city").value;
    console.log(city_zipCode);
    city_zipCode.forEach(function(CZ){
        if(CZ.city==cityName){
            document.getElementById("id_zipcode").value = CZ.zipcode;
            return;
        }
    });
}