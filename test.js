var fs = require('fs')

var ipa_xsampa = JSON.parse(fs.readFileSync("./ipa_xsampa_map.json"))
var sassc_ipa = JSON.parse(fs.readFileSync("./sassc_ipa.json"))

var ipa_xsampa_map = {}

for (var pair of ipa_xsampa) {
  ipa_xsampa_map[pair[0]] = pair[1]
}
for (var pair of sassc_ipa) {
  for (var c of pair[1]) {
    if (!ipa_xsampa_map.hasOwnProperty(c)) {
    } else {
      console.log(ipa_xsampa_map[c])
    }
  }
}
