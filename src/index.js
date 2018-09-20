/**
 * @param preferences - an array of integers. Indices of people, whom they love
 * @returns number of love triangles
 */
module.exports = function getLoveTrianglesCount(preferences = []) {
	var a=preferences
	var c=0
	for (var i=1;i<a.length+1;i++) {
	if (a[i-1]===a[a[a[a[i-1]-1]-1]-1] && a[i-1]!=a[a[i-1]-1]) {
		delete  a[a[a[i-1]-1]-1]
		c++
		}
	}
  return c
};
