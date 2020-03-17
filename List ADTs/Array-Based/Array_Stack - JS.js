/**
 * initialize your data structure here.
 * NOTE: THERE ARE MOST LIKELY OTHER BUGS THAT HAVE NOT YET BEEN ENCOUNTERED YET
 */

// initialize list with 10 elements.
// double list size whenever stack approaches limit


// pop() removes the top element
// push() pushes to top index

// store the pushed element at the end of array
// so that popping it is fast O(1) operation
var MinStack = function() {
  this.stack = new Array(10).fill(0);
  this.count = 0
  this.len = 10
  this.top_index = -1
};


/** 
* @return {MinStack}
*/
MinStack.prototype.upsize = function() {
  newstack = new Array(this.len * 2).fill(null)
  for(i=0; i<this.count; i++) {
      newstack[i] = this.stack[i]
  }
  this.stack = newstack
}

/** 
* @return {MinStack}
*/
MinStack.prototype.downsize = function() {
  newstack = new Array(this.len / 2)
  if(this.count == 0) {
      this.stack = newstack
  }
  else {
      for(i=0; i < this.count; i++) {
          newstack[i] = this.stack[i]
      } 
  }

}

/** 
* @return {boolean}
*/
MinStack.prototype.isfull = function() {
  return this.count == this.len
}

/** 
* @return {boolean}
*/
// if empty, restore stack size down to default 10 items
MinStack.prototype.isEmpty = function() {
  return this.count == 0
}

/** 
* @param {number} x
* @return {void}
*/
MinStack.prototype.push = function(x) {

if(this.isfull()) {
    this.upsize()
}

this.stack[this.count] = x
this.count += 1
this.len *= 2
this.top_index += 1
  
};

/**
* @return {void}
*/
MinStack.prototype.pop = function() {
  if(this.isEmpty()) {
      return false
  }
  else {
    // downsize
    if(this.count < (this.len / 2)) {
      this.downsize
      this.len /= 2
    }
    item = this.stack[this.top_index]
    this.top_index -= 1
    this.count -= 1
    return item
  }
};

/**
* @return {number}
*/
MinStack.prototype.top = function() {
  return this.stack[this.top_index]
};

/**
* @return {number}
*/
MinStack.prototype.getMin = function() {
  min = Number.MAX_SAFE_INTEGER
  for(i=0; i<this.count; i++) {
      if(this.stack[i] < min)
          min = this.stack[i]
  }
  return min
}

var minStack = new MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
console.log(minStack.getMin())  // --> Returns -3.
minStack.pop();
console.log(minStack.top())      // --> Returns 0.
console.log(minStack.getMin())   // --> Returns -2.