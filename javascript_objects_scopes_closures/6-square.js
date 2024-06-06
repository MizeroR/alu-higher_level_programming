#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
<<<<<<< HEAD
	  charPrint (c) {
		      if (c === undefined) {
			            this.print();
			          } else {
					        for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
					      }
		    }
=======
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
>>>>>>> 52f9a3d68502307fd5dc0e260f31b82df63db92d
};
