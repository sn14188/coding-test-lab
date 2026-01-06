function solution(prices) {
  const answer = new Array(prices.length).fill(0);
  const stack = [0]; // why const

  for (let i = 1; i < prices.length; i++) {
    const price = prices[i];

    top = prices[stack[stack.length - 1]];
    if (top <= price) {
      stack.push(i);
    } else {
      while (prices[stack[stack.length - 1]] > price) {
        top_idx = stack.pop();
        duration = i - top_idx;
        answer[top_idx] = duration;
      }
      stack.push(i);
    }
  }

  last_Idx = prices.length - 1;
  while (stack.length > 0) {
    idx = stack.pop();
    answer[idx] = last_Idx - idx;
  }

  return answer;
}

console.assert(
  JSON.stringify(solution([1, 2, 3, 2, 3])) === JSON.stringify([4, 3, 1, 1, 0])
);
console.assert(
  JSON.stringify(solution([1, 2, 7, 10, 12, 4, 2])) ===
    JSON.stringify([6, 5, 3, 2, 1, 1, 0])
);

console.log("All tests passed!");
