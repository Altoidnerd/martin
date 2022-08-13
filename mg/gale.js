
Wh1te T1ger
2:48 PM (0 minutes ago)
to me

var minstake   = 0.00000001;  // valor base

//-----------------------------------------

var autorounds = 500;         // n° de rolls

//======================================================

// if (profit > profit_max) {

    //     error_title = "Maximum profit exceeded";

    //     error_info = "Maximum profit: " + number_format(profit_max, devise_decimal);

    //     error_value = "Maximum profit exceeded - Maximum profit: " + number_format(profit_max, devise_decimal);

    //     error = true;

    // }

    // else if (amount > balance) {

    //     error_title = "Bet amount";

    //     error_info = "Maximum bet: " + number_format(balance, devise_decimal);

    //     error_value = "Bet amount - Maximum bet: " + number_format(balance, devise_decimal);

    //     error = true;

    // }

var handbrake  = 0.000010;  // valor lose pause game

var autoruns   = 1;

    // else if (amount > bet_max) {

    //     error_title = "Bet amount";

    //     error_info = "Maximum bet: " + number_format(bet_max, devise_decimal);

    //     error_value = "Bet amount - Maximum bet: " + number_format(bet_max, devise_decimal);

    //     error = true;

    // }

    // else if (amount < bet_min) {

    //     error_title = "Bet amount";

    //     error_info = "Minimum bet: " + number_format(bet_min, devise_decimal);

    //     error_value = "Bet amount - Minimum bet: " + number_format(bet_min, devise_decimal);

    //     error = true;

    // }

function playnow() {

       if (autoruns > autorounds ) { console.log('Limit reached'); return; }

       document.getElementById('double_your_btc_bet_hi_button').click();

       setTimeout(checkresults, 50);

       return;}

function checkresults() {

       if (document.getElementById('double_your_btc_bet_hi_button').disabled === true) {

              setTimeout(checkresults, 50);

              return;

       }

       var stake = document.getElementById('double_your_btc_stake').value * 1;

       var won = document.getElementById('double_your_btc_bet_win').innerHTML;

       if (won.match(/(\d+\.\d+)/) !== null) { won = won.match(/(\d+\.\d+)/)[0]; } else { won = false; }

       var lost = document.getElementById('double_your_btc_bet_lose').innerHTML;

       if (lost.match(/(\d+\.\d+)/) !== null) { lost = lost.match(/(\d+\.\d+)/)[0]; } else { lost = false; }

       if (won && !lost) { stake = minstake; console.log('Bet #' + autoruns + '/' + autorounds + ': Won  ' + won  + ' Stake: ' + stake.toFixed(8)); }

       if (lost && !won) { stake = lost * 2.1; console.log('Bet #' + autoruns + '/' + autorounds + ': Lost ' + lost + ' Stake: ' + stake.toFixed(8)); }

       if (!won && !lost) { console.log('Something went wrong'); return; }

       document.getElementById('double_your_btc_stake').value = stake.toFixed(8);

       autoruns++;

       if (stake >= handbrake) {

              document.getElementById('handbrakealert').play();

              console.log('Handbrake triggered! Execute playnow() to override');

           return;

       }

       setTimeout(playnow, 25);

       return;


       }playnow()
