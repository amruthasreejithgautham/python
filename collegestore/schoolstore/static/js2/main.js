(function($) {

  $('#reset').on('click', function(){
      $('#register-form').reset();
  });

})(jQuery);
const deptDataBox = document.getElementById('cars-data-box')
$.ajax({
    type: 'GET',
    url: '/cars-json/',
    success: function(response){
        console.log(response.data)
        const deptData = response.data
        deptData.map(item->{
        const option = document.createElement('option')
        option.textContent = item.name
        option.setAttribute('class','item')
        option.setAttribute('value', item.name)
        deptDataBox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
        }
})