import type { NextConfig } from "next";

// https://nextjs.org/docs/messages/next-image-unconfigured-host

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [new URL('https://storage.googleapis.com/zootasks_test_us/**')],
  },
};

export default nextConfig;
