function indexEqualsValue(arr) {
  let start = 0;
  let end = arr.length;
  let result = -1;
  
  if (arr[start] > end) {
    return -1
  }

  while (start < end) {
    let mid = Math.floor((end + start) / 2);
    if (arr[mid] > mid) {
      end = mid;
    } else if (arr[mid] < mid) {
      start = mid + 1;
    } else {
      result = mid;
      end = mid;
    }
  }

  return result;
}

console.log(indexEqualsValue([-5, 1, 2, 3, 4, 5, 7, 10, 15]))
