var jsonData = '[{"Name":"Peter","Job":"Programmer"},{"Name":"John","Job":"Programmer"},{"Name":"Kevin","Job":"Scientist"}]';

UpdateView("#testDiv",jsonData);

function UpdateView(divId,jsonData){
var htmlTemplate = '<div class="card"><p>My name is: {0}</p><!-- another code --><p>My job is: {1}</p><!-- some more code --></div>';
var dataList= JSON.parse(jsonData);

var html ="";
dataList.forEach(function(item){

var temp = htmlTemplate.replace("{0}",item.Name);
temp =temp.replace('{1}',item.Job);
html += temp;

});
console.log(html)
$(divId).html(html);
}
