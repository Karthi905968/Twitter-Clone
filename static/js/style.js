
$(function(){
    $('.heart').click(function(){
      $(this).toggleClass('active');
      
    })
  })

  $(function(){
    $('.dots').click(function(){
      $(this).next().toggle();
      
      
    })
  })