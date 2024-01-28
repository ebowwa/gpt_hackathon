"use client";
import React, { useState } from 'react';
import useSWR, { mutate } from 'swr';
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import Link from "next/link";

const fetcher = async (url, data) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    const error = new Error('An error occurred while fetching the data.');
    error.info = await response.json();
    error.status = response.status;
    throw error;
  }

  return response.json();
};

export default function Component() {
  const [prompt, setPrompt] = useState('');

  // SWR key
  const swrKey = ['/process_content', { inquiry: prompt }];

  // SWR hook for revalidation
  const { data, error } = useSWR(swrKey, fetcher, {
    revalidateOnFocus: false,
    shouldRetryOnError: false,
    dedupingInterval: 2000,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await mutate(swrKey, () => fetcher(swrKey[0], swrKey[1]), false);
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
