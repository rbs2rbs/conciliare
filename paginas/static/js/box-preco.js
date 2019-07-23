$('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var plano = button.data('plano') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    // modal.find('.modal-title').text('New message to ' + recipient)
    // modal.find('.modal-body #name').val("renan")
    modal.find('.modal-body #msg_subject').val("Planos - conciliare")
    modal.find('.modal-body #message').val(plano)
    // modal.find('.modal-body #name').val("renan")
  })

$('#submit-box').on('click', function(){
    var mensagem = $('#exampleModal').find('.modal-body #message')
    mensagem.val(mensagem.val() + $('#numero').val())
    $('.box-load').removeClass();
})