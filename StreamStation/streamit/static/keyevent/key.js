
$(function() {
    var FADE_TIME = 150; // ms
    var $window = $(window);
    var COLORS = [
        '#e21400', '#91580f', '#f8a700', '#f78b00',
        '#58dc00', '#287b00', '#a8f07a', '#4ae8c4',
        '#3b88eb', '#3824aa', '#a700ff', '#d300e7'
    ];
    var $keyMessages = $('.keymessages'); // Key Messages area
    var $inputMessage = $('.inputMessage'); // Input message input box
    var keyPressed = false;
    var userNames = ["Bryan","Ryan", "Alan", "Dvaid", "Linus", "Kobe"];
    var event2key = {'65':'a', '66':'b', '67':'c', '68':'d', '69':'e', '70':'f', '71':'g', '72':'h', '73':'i', '74':'j', '75':'k', '76':'l', '77':'m', '78':'n', '79':'o', '80':'p', '81':'q', '82':'r', '83':'s', '84':'t', '85':'u', '86':'v', '87':'w', '88':'x', '89':'y', '90':'z', '37':'left', '39':'right', '38':'up', '40':'down', '13':'enter', '32':'space','48':'0','49':'1','50':'2','51':'3','52':'4','53':'5','54':'6','55':'7','56':'8','57':'9'};
    
    function getRandomUser() {
        return userNames[Math.floor(Math.random() * 100) % userNames.length];
    }

    function getRandomColor() {
        var hash = Math.floor(Math.random() * 100)
        // Calculate color
        var index = Math.abs(hash % COLORS.length);
        return COLORS[index];
    }

    function addMessageElement(parent, el) {
        var $parent = $(parent);
        var $el = $(el);

        $el.hide();
        $parent.append($el);
        $el.fadeIn(FADE_TIME);
        $parent[0].scrollTop = $parent[0].scrollHeight;

    }
    function formatMessage(message, user) {
        var $usernameDiv = $('<span class="username"/>')
            .text(user)
            .css('color', getRandomColor());
        var $messageBodyDiv = $('<span class="messageBody">')
                .text(message);

        // var $keyboard = $('<i class="fa fa-keyboard-o" aria-hidden="true"></i>&nbsp;')

        var $messageDiv = $('<li class="message"/>')
                .append($usernameDiv, $messageBodyDiv);
        return $messageDiv;
    }

    $window.keydown(function (event) {
        var keycode = event.which || event.keyCode;
        if (!$inputMessage.is(":focus")) {
            if (keycode in event2key && !keyPressed) {
                var myKey = event2key[keycode];
                $("#"+myKey).addClass('active');
                addMessageElement($keyMessages, formatMessage(myKey, "You"));
                
                event.preventDefault(); // Prevent arrow-key from scrolling window

            }
            keyPressed = true;
        }
        
    });
    $window.keyup(function (event) {
        var keycode = event.which || event.keyCode;
        if (keycode in event2key) {
            var myKey = event2key[keycode];
            $("#"+myKey).removeClass('active');
            keyPressed = false;
        }
    });

    (function loop() {
        var rand = Math.round(Math.random() * (1000 - 500)) + 200;
        setTimeout(function() {
                var keys = Object.keys(event2key);
                var myKey = event2key[keys[ keys.length * Math.random() << 0]];
                addMessageElement($keyMessages, formatMessage(myKey, getRandomUser()));
                if ($keyMessages.children().length > 10) {
                    $keyMessages.find('li:first').remove();
                }
                loop();  
        }, rand);
    }());

});