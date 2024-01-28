import React from "react";
// import { Layout } from "./layout";
import { Button } from '@/components/ui/button';
import { IconMessageCircle } from 'lucide-react';

// This page is a simple placeholder for the "Response" section
const ResponsePage = () => {
  return (
    <Layout>
      <div className="flex flex-col items-center justify-center h-full p-4">
        <IconMessageCircle className="text-6xl text-green-500 mb-4" />
        <h1 className="text-2xl font-semibold">Response Page</h1>
        <p className="text-lg text-gray-600 mt-2">Your response has been recorded. Thank you!</p>
        <Button className="mt-4">Back to Home</Button>
      </div>
    </Layout>
  );
};

export default ResponsePage;
