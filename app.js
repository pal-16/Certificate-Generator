var express = require('express'),
    bodyParser = require('body-parser');
/*    passport = require('passport'),
    passportLocal = require('passport-local'),
    passportLocalMongoose = require('passport-local-mongoose'),
    request = require('request')

var app = express()
mongoose.connect('mongodb://localhost/ink_overflow')

*/
var app = express();
//const upload = multer({dest: __dirname + '/uploads/images'});



app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }))
app.get('/', function (req, res) {
    res.render('form')
})
const request = require('request')

app.post('/submit', function (req, res) {
    console.log("===============");
    console.log(req.body.userId);
    request.post(
        'https://certificateyay-test.herokuapp.com/dataUploads',
        {
            json: {
                userId: req.body.userId,
                certiTemplate: req.body.certiTemplate,
                csvData: req.body.csvData,
                location: req.body.location
            }
        },
        (error, res, body) => {
            if (error) {
                console.error(error)
                return
            }
            console.log(`statusCode: ${res.statusCode}`)
            console.log(body)
        })
})
app.listen(process.env.PORT || 3000, function () {
    console.log('server is running ....')
})


