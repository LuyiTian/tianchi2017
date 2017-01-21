// please install node, use 'npm install pinyin'

var pinyin = require('pinyin');
// input Chinese string
var chinese = '';

var result = pinyin(chinese, {
	style: pinyin.STYLE_NORMAL
});
// finally, get pinyin string
var finalResult = result.join('');