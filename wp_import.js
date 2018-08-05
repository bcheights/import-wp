require("dotenv").config();
const WPAPI = require("wpapi");
const newWP = WPAPI({
  endpoint: "http://18.219.114.43/wp-json",
  username: process.env.WP_USER,
  password: process.env.WP_PW
});
const oldWP = WPAPI({
  endpoint: "http://bcheights.com/wp-json"
});

async function test() {
  const posts = await oldWP.posts();
  // console.log(posts);
  console.log(posts.length);
}

test();
