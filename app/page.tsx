"use client";
import { useState } from 'react';
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Component() {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await fetch('/process_content', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ inquiry: prompt }),
      });
      const data = await response.json();
      console.log(data); // You can handle the response here, such as showing a download link
    } catch (error) {
      console.error('Error:', error);
    }
  };
  const handleChange = (e) => {
    setPrompt(e.target.value);
  };

  return (
    <main className="flex flex-col items-center justify-center h-screen px-4 py-12 bg-gray-100 dark:bg-gray-900">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100">
          YouTube-Short-inator
        </h1>
        <p className="text-gray-600 dark:text-gray-400">
          Create the perfect YouTube Short in an instant, with the power of AI
        </p>
      </div>
      <div className="flex w-full max-w-md items-center space-x-2 mt-8">
        <Input placeholder="Enter your prompt here" type="text" value={prompt}
          onChange={handleChange}/>
        <Link href="/result">
          <Button type="submit" onClick={handleSubmit}>Submit</Button>
        </Link>
      </div>
    </main>
  );
}
